import multiprocessing
from multiprocessing import Pool
import subprocess
from drivescanner import ingest, rules
from typing import Tuple
import tqdm
import json
import functools


def _scan_file(
    file_tuple: Tuple[str, dict],
    NER: bool = False,
    result_filename: str = "processed_files",
) -> Tuple[str, dict]:
    """
    It takes a tuple of a file name and a dictionary of file information, reads the file, and then
    updates the dictionary with the results of the file scan

    Args:
      file_tuple (Tuple): Tuple

    Returns:
      A tuple of the dictkey and the file_dict
    """
    # input test before we go
    assert isinstance(file_tuple, tuple), "Input should be a tuple"

    dictkey = file_tuple[0]
    file_dict = file_tuple[1]

    content, errormsg = ingest.ingest_file(
        file_dict["filepath"], file_dict["extension"]
    )

    # unsync file from OneDrive (unclear if it works for other cloud providers)
    subprocess.run('attrib +U -P "' + file_dict["filepath"] + '"')

    if content is None:
        file_dict["content_processed"] = False
        file_dict["processing_error"] = errormsg
    else:
        file_dict["content_processed"] = True

        if NER == True:
            try:
                file_dict["entities"] = rules.extract_NER(content, NER_select=["PERSON"])
                rules_dict = rules.search_text_file(content)
                file_dict.update(rules_dict)
            except:
                file_dict["content_processed"] = False
                file_dict["processing_error"] = "file processing failed"
        else:
            try:
                rules_dict = rules.search_text_file(content)
                file_dict.update(rules_dict)
            except:
                file_dict["content_processed"] = False
                file_dict["processing_error"] = "file processing failed"

    # write result to file as a new line
    with open(f"{result_filename}.jsonl", "a") as f:
        f.write(json.dumps({dictkey: file_dict}) + "\n")

    return (dictkey, file_dict)


def scan_drive(
    dict_files: dict, NER: bool = False, result_filename="processed_files"
) -> dict:
    """
    The function "scan_drive" scans a dictionary of files using multiprocessing and returns the results
    as a dictionary.

    Args:
      dict_files (dict): A dictionary containing file paths as keys and file contents as values.
      NER (bool): NER stands for Named Entity Recognition, which is a technique used in natural language
    processing to identify and extract named entities (such as people, organizations, and locations)
    from text. In this context, it likely refers to whether or not the function should perform NER on
    the files being scanned. Defaults to False

    Returns:
      The function `scan_drive` returns a dictionary containing the results of scanning each file in the
    input dictionary `dict_files` using the `_scan_file` function. The `NER` parameter is used to
    determine whether or not to perform Named Entity Recognition during the scanning process. The
    function uses multiprocessing to speed up the scanning process by utilizing all available CPU cores.
    """
    pool = Pool(multiprocessing.cpu_count())
    results = pool.starmap(
        _scan_file,
        tqdm.tqdm(
            [(i, NER, result_filename) for i in dict_files.items()],
            total=len(dict_files),
        ),
    )

    pool.close()
    pool.join()

    return dict(results)
