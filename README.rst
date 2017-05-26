**********
PyInstance
**********

Python Object Instance Management

It is sometimes necessary to manage the instances that are used through a project.
Often this is done using a singleton pattern that only allows a single instance to
exist. However, sometimes it's desireable to be able to have multiple instances that
can be easily distinguished and ensure that the same instance can be reliably accessed
at the appropriate times.

This is where PyInstance comes in. PyInstance applies a modified singleton design
pattern where each singleton instance is identifiable by the session name. Each
session is reference counted with the deletion of the last instance clearing out
the entire record. The only caveat is that the session name is the first parameter
to the object's ``__init__`` method.
