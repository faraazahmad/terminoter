import urwid

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

pallette = [
            ('banner', 'black', 'light gray'),
            ('streak', 'black', 'dark red'),
            ('bg', 'black', 'dark blue')]

txt = urwid.Text(('banner', u" Hello World "), align = 'center')
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()
