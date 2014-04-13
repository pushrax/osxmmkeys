=========
osxmmkeys
=========

osxmmkeys is a simple Python library for handling media keys on OS X.
The default behaviour can be prevented and overridden entirely.

Supported keys are:

- ``play_pause``
- ``next_track``
- ``prev_track``
- ``mute``
- ``volume_down``
- ``volume_up``
- ``backlight_down``
- ``backlight_up``
- ``kb_backlight_down``
- ``kb_backlight_up``


Usage:
------

.. code-block:: python
    import osxmmkeys

    def play_pause():
        print("Play/pause key was pressed")

    tap = osxmmkeys.Tap()
    tap.on('play_pause', play_pause)
    tap.run()
