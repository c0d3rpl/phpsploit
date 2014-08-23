import objects
import datatypes


class CACHE_SIZE:
    """
    This core configuration setting limits the
    session's maximum size.

    While using the phpsploit framework, some usage
    informations are stored, such as commands history.
    Changing this limit ensures that the session, if
    saved whith the 1session save` command will not
    exceed the given size.

    USE CASES:
      * The `history` feature takes this setting into
        account for limiting the number of saved
        command lines.
    """
    type = objects.settings.MultiLineBuffer

    def setter(self, value):
        return datatypes.ByteSize(value)

    def default_value(self):
        raw_value = "1 MiB"
        return self.setter(raw_value)