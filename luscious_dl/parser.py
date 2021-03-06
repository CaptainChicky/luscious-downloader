# -*- coding: utf-8 -*-
from typing import Optional, Union, List, Callable

from luscious_dl.logger import logger


def is_a_valid_id(id_: Union[str, int]) -> bool:
  """
  Check if it is a valid id.
  :param id_: id in string or int format
  :return: bool
  """
  try:
    if isinstance(int(id_), int):
      return True
  except (ValueError, TypeError):
    return False


def extract_album_id(album_url: str) -> Optional[int]:
  """
  Extract id from album url.
  :param album_url: album url
  :return: album id
  """
  try:
    split = 2 if album_url.endswith('/') else 1
    album_id = album_url.rsplit('/', split)[1].rsplit('_', 1)[1]
    if is_a_valid_id(album_id):
      return int(album_id)
    else:
      raise Exception('ValueError')
  except Exception as e:
    logger.critical(f"Couldn't resolve album ID of {album_url}\nError: {e}")
    return None


def extract_user_id(user_url: str) -> Optional[int]:
  """
  Extract id from user url.
  :param user_url: user url
  :return: user id
  """
  try:
    split = 2 if user_url.endswith('/') else 1
    user_id = user_url.rsplit('/', split)[1]
    if is_a_valid_id(user_id):
      return int(user_id)
    else:
      raise Exception('ValueError')
  except Exception as e:
    logger.critical(f"Couldn't resolve user ID of {user_url}\nError: {e}")
    return None


def extract_ids_from_list(iterable: List[Union[str, int]], extractor: Callable[[str], Optional[int]]) -> List[int]:
  """
  Extract ids from list containing urls/ids.
  :param iterable: list containing urls/ids
  :param extractor: extraction function
  :return: A list containing the ids
  """
  return list(filter(None, set(int(item) if is_a_valid_id(item) else extractor(item) for item in iterable)))
