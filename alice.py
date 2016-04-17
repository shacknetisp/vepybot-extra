# -*- coding: utf-8 -*-
"""
Copyright (c) 2016 Vepybot Developers

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

"""
Add the aiml-en-us-foundation-alice directory to your userdata to run this.
"""

import bot
import aiml
import glob

if not hasattr(bot, 'module_store_alice_kernel'):
    print("Loading ALICE")
    bot.module_store_alice_kernel = aiml.Kernel()
    for file in glob.glob(
        bot.userdata + "/aiml-en-us-foundation-alice/*.aiml"):
            bot.module_store_alice_kernel.learn(file)


class Module(bot.Module):

    index = "alice"

    def register(self):

        self.addcommand(
            self.go,
            "alice",
            "Communicate with Alice (http://alicebot.org).", ["[input]"])

    def go(self, context, args):
        args.default("input", "")
        return bot.module_store_alice_kernel.respond(
            args.getstr('input')) or '...'

bot.register.module(Module)
