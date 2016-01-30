"""
By acz13 
Requires the pyjokes module (http://pyjok.es)

Copyright © 2015 Vepybot Developers
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import bot
import pyjokes

class Module(bot.Module):

    index = "pyjokes"

    def register(self):

        self.addcommand(
            self.pyjokes,
            "joke",
            "return a pyjoke.",
            ["[category]"])
        self.addsetting('language', 'en')
        self.addsetting('adult', False)

    def pyjokes(self, context, args):
        args.default("category", "neutral")
        if args.getstr("category") == 'adult' and not self.getsetting('adult'):
            return 'Adult jokes are not allowed on this channel'
        else:
            try:
                return "%s" % (pyjokes.get_joke(self.getsetting('language'),
                                                args.getstr("category")))
            except pyjokes.pyjokes.CategoryNotFoundError as err:
                return err
            except pyjokes.pyjokes.LanguageNotFoundError as err:
                return err
bot.register.module(Module)
