from datadog.api.resources import ActionAPIResource


class Host(ActionAPIResource):
    """
    A wrapper around Host HTTP API.
    """
    _class_url = '/host'

    @classmethod
    def mute(cls, host_name, **body):
        """
        Mute a host.

        :param host_name: hostname
        :type host_name: string

        :param end: timestamp to end muting
        :type end: POSIX timestamp

        :param override: if true and the host is already muted, will override\
         existing end on the host
        :type override: bool

        :param message: message to associate with the muting of this host
        :type message: string

        :returns: Dictionary representing the API's JSON response

        """
        return super(Host, cls)._trigger_class_action('POST', 'mute', host_name, **body)

    @classmethod
    def unmute(cls, host_name):
        """
        Unmute a host.

        :param host_name: hostname
        :type host_name: string

        :returns: Dictionary representing the API's JSON response

        """
        return super(Host, cls)._trigger_class_action('POST', 'unmute', host_name)
