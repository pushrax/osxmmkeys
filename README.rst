=========
osxmmkeys
=========

osxmmkeys is a simple Python library for handling media keys on OS X.
Key presses can be observed with no side effects, or have their default
behaviours overridden entirely.

Installation
------------

To install osxmmkeys with pip, use:

.. code:: bash

    $ pip install osxmmkeys

Usage
-----

Simple example:

.. code:: python

    import osxmmkeys

    def handler():
        print("Play/pause key was pressed")

    tap = osxmmkeys.Tap()
    tap.on('play_pause', handler)
    tap.run()

Threaded example:

.. code:: python

    import osxmmkeys, time

    def handler():
        print("Play/pause key was pressed")

    tap = osxmmkeys.Tap()
    tap.on('play_pause', handler)
    tap.start()

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        tap.stop()

Supported key names:

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
