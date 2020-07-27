# -*- coding: utf-8 -*-
"""
structs metadata module.
"""


class DocstringMetadata:
    """
    docstring metadata class.
    """

    def __init__(self, **options):
        """
        initializes an instance of DocstringMetadata.

        :keyword str short_description: short description.
        :keyword str long_description: long description.
        :keyword list params: required parameters.
        :keyword list options: optional parameters.
        :keyword list exceptions: possible exceptions.
        :keyword str return_type: return type.
        :keyword str return_description: return value description
        :keyword list custom_values: custom values.
        """

        self._short_description = options.get('short_description') or ''
        self._long_description = options.get('long_description') or ''
        self._params = options.get('params') or []
        self._options = options.get('options') or []
        self._exceptions = options.get('exceptions') or []
        self._return_type = options.get('return_type') or ''
        self._return_description = options.get('return_description') or ''
        self._custom_values = options.get('custom_values') or []

    @property
    def short_description(self):
        """
        gets the short description of this docstring metadata.

        :rtype: str
        """

        return self._short_description

    @property
    def long_description(self):
        """
        gets the long description of this docstring metadata.

        :rtype: str
        """

        return self._long_description

    @property
    def full_description(self):
        """
        gets the full description of this docstring metadata.

        it returns the short and long descriptions if both are available.

        :rtype: str
        """

        if self.has_short_description and self.has_long_description:
            return '{short}\n\n{long}'.format(short=self.short_description,
                                              long=self.long_description)

        if self.has_short_description:
            return self.short_description

        if self.has_long_description:
            return self.long_description

        return ''

    @property
    def params(self):
        """
        gets the required params of this docstring metadata.

        :rtype: list
        """

        return self._params

    @property
    def options(self):
        """
        gets the optional params of this docstring metadata.

        :rtype: list
        """

        return self._options

    @property
    def exceptions(self):
        """
        gets the exceptions of this docstring metadata.

        :rtype: list
        """

        return self._exceptions

    @property
    def return_type(self):
        """
        gets the return type of this docstring metadata.

        :rtype: str
        """

        return self._return_type

    @property
    def return_description(self):
        """
        gets the return description of this docstring metadata.

        :rtype: str
        """

        return self._return_description

    @property
    def custom_values(self):
        """
        gets the custom values of this docstring metadata.

        :rtype: list
        """

        return self._custom_values

    @property
    def has_short_description(self):
        """
        gets a value indicating that this docstring metadata has short description.

        :rtype: bool
        """

        return len(self.short_description) > 0

    @property
    def has_long_description(self):
        """
        gets a value indicating that this docstring metadata has long description.

        :rtype: bool
        """

        return len(self.long_description) > 0

    @property
    def has_full_description(self):
        """
        gets a value indicating that this docstring metadata has full description.

        :rtype: bool
        """

        return len(self.full_description) > 0

    @property
    def has_params(self):
        """
        gets a value indicating that this docstring metadata has params.

        :rtype: bool
        """

        return len(self.params) > 0

    @property
    def has_options(self):
        """
        gets a value indicating that this docstring metadata has options.

        :rtype: bool
        """

        return len(self.options) > 0

    @property
    def has_exceptions(self):
        """
        gets a value indicating that this docstring metadata has exceptions.

        :rtype: bool
        """

        return len(self.exceptions) > 0

    @property
    def has_return_type(self):
        """
        gets a value indicating that this docstring metadata has return type.

        :rtype: bool
        """

        return len(self.return_type) > 0

    @property
    def has_return_description(self):
        """
        gets a value indicating that this docstring metadata has return description.

        :rtype: bool
        """

        return len(self.return_description) > 0

    @property
    def has_custom_values(self):
        """
        gets a value indicating that this docstring metadata has custom values.

        :rtype: bool
        """

        return len(self.custom_values) > 0
