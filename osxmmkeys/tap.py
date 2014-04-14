import AppKit
import Quartz
import threading


class Tap(threading.Thread):
    MEDIA_EVENT_SUBTYPE = 8
    KEY_CODES = {
        16: 'play_pause',
        19: 'next_track',
        20: 'prev_track',
        7: 'mute',
        1: 'volume_down',
        0: 'volume_up',
        3: 'backlight_down',
        2: 'backlight_up',
        22: 'kb_backlight_down',
        21: 'kb_backlight_up',
    }

    def __init__(self):
        self._handlers = {key: [] for code, key in self.KEY_CODES.items()}
        super(Tap, self).__init__()

    def on(self, event, handler):
        self._handlers[event].append(handler)

    def run(self):
        tap = Quartz.CGEventTapCreate(
            Quartz.kCGSessionEventTap,
            Quartz.kCGHeadInsertEventTap,
            Quartz.kCGEventTapOptionDefault,
            Quartz.CGEventMaskBit(AppKit.NSSystemDefined),
            self._handle_event_tap,
            None
        )

        loop_source = Quartz.CFMachPortCreateRunLoopSource(None, tap, 0)
        Quartz.CFRunLoopAddSource(
            Quartz.CFRunLoopGetCurrent(),
            loop_source,
            Quartz.kCFRunLoopDefaultMode,
        )

        self.loop_ref = Quartz.CFRunLoopGetCurrent()
        Quartz.CFRetain(self.loop_ref)

        Quartz.CGEventTapEnable(tap, True)
        Quartz.CFRunLoopRun()  # Only returns after stop() is called.

    def stop(self):
        Quartz.CFRunLoopStop(self.loop_ref)
        Quartz.CFRelease(self.loop_ref)
        self.join()

    def _handle_event_tap(self, proxy, cg_event_type, cg_event, refcon):
        ns_event = AppKit.NSEvent.eventWithCGEvent_(cg_event)
        if not self._handle_event(ns_event):
            return cg_event  # Allow event to propagate.

    def _handle_event(self, event):
        if event.subtype() != self.MEDIA_EVENT_SUBTYPE:
            return

        data = event.data1()
        code = (data & 0xFFFF0000) >> 16
        state = (data & 0xFF00) >> 8

        if state != AppKit.NSKeyDown or code not in self.KEY_CODES:
            return

        for handler in self._handlers[self.KEY_CODES[code]]:
            if handler() == False:
                return True

