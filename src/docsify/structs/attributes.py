# -*- coding: utf-8 -*-
"""
structs attributes module.
"""


class AttributeBase:
    """
    attribute base class.
    """

    HANDLERS = ()

    def render(self, **options):
        """
        renders the current attribute into its string representation.

        :raises NotImplementedError: not implemented error.

        :rtype: str
        """

        raise NotImplementedError()
