# Copyright (C) 2023 Bootloader.  All rights reserved.
#
# This software is the confidential and proprietary information of
# Bootloader or one of its subsidiaries.  You shall not disclose this
# confidential information and shall use it only in accordance with the
# terms of the license agreement or other applicable agreement you
# entered into with Bootloader.
#
# BOOTLOADER MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE
# SUITABILITY OF THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR
# A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.  BOOTLOADER SHALL NOT BE
# LIABLE FOR ANY LOSSES OR DAMAGES SUFFERED BY LICENSEE AS A RESULT OF
# USING, MODIFYING OR DISTRIBUTING THIS SOFTWARE OR ITS DERIVATIVES.

from __future__ import annotations

import hashlib
import json
import logging
import os
from pathlib import Path


class UAsset:
    def __init__(
            self,
            asset_name: str,
            asset_class_path: str,
            package_name: str,
            dependencies: list[str] or None):
        """
        Build a new {@link UAsset}.


        :param asset_name: The name of the asset without the package.

        :param asset_class_path: The path name of the asset’s class.

        :param package_name: The name of the package in which the asset is
            found.

        :param dependencies: The list of names of the packages that the asset
            depends on.
        """
        self.__asset_name = asset_name
        self.__asset_class_path = asset_class_path
        self.__package_name = package_name
        self.__dependencies = dependencies

    @property
    def asset_class_path(self) -> str:
        """
        Return the path name of the asset's class.

        Examples:

        ```text
        /Script/Engine/SkeletalMesh
        /Script/Engine/Skeleton
        /Script/Engine/Texture2D
        ```

        :return: The path name of the asset's class.
        """
        return self.__asset_class_path

    @property
    def asset_name(self) -> str:
        """
        Return the name of the asset.


        :return: The name of the asset without the package.
        """
        return self.__asset_name

    @property
    def dependencies(self) -> list[str] or None:
        """
        Return the list of names of the packages that the asset depends on.


        :return: The list of names of the packages that the asset depends on.
        """
        return self.__dependencies

    @staticmethod
    def from_json(payload: any):
        if isinstance(payload, str):
            payload = json.loads(payload)

        # @todo: Check data consistency (type, path, list of strings, etc.)
        return UAsset(
            payload['asset_name'],
            payload['asset_class_path'],
            payload['package_name'],
            payload['dependencies']
        )

    def to_json(self) -> any:
        return {
            "asset_name": self.__asset_name,
            "asset_class_path": self.__asset_class_path,
            "package_name": self.__package_name,
            "dependencies": self.__dependencies
        }

    @property
    def package_name(self) -> str:
        """
        Return the name of the package in which the asset is found.


        :return: The name of the package in which the asset is found.
        """
        return self.__package_name


class UAssetFile:
    FILE_READ_BLOCK_SIZE = 4096

    def __init__(
            self,
            asset,
            file_path_name):
        if not os.path.exists(file_path_name):
            error_message = f"The file {file_path_name} of the asset {asset.asset_name} doesn't exist"
            logging.error(error_message)
            raise FileNotFoundError(error_message)

        self.__asset = asset
        self.__file_path_name = file_path_name
        self.__file_status = None  # This attribute is lazy loaded (cf. property `file_status`)
        self.__file_checksum = None  # This attribute is lazy loaded (cf. property `file_checksum`)

    def __calculate_file_checksum(self) -> str:
        sha256_hash = hashlib.sha256()

        with open(self.__file_path_name, 'rb') as fd:
            # Read and update hash string value in blocks of bytes.
            for byte_block in iter(lambda: fd.read(self.FILE_READ_BLOCK_SIZE), b''):
                sha256_hash.update(byte_block)

        return sha256_hash.hexdigest()

    @property
    def asset(self) -> UAsset:
        return self.__asset

    @property
    def file_checksum(self) -> str:
        if self.__file_checksum is None:
            self.__file_checksum = self.__calculate_file_checksum()

        return self.__file_checksum

    @property
    def file_path_name(self) -> Path:
        return self.__file_path_name

    @property
    def file_status(self) -> os.stat_result:
        """
        Return the detailed status of the asset file.


        :return: The detailed status of the asset file.
        """
        if self.__file_status is None:
            self.__file_status = Path.stat(self.__file_path_name)

        return self.__file_status

    def to_json(self) -> any:
        payload = self.__asset.to_json()
        payload['file_size'] = self.file_status.st_size
        payload['file_checksum'] = self.file_checksum
        return payload


