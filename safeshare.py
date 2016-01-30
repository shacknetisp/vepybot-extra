"""
By acz13

The MIT License (MIT)
Copyright (c) 2016 Vepybot Developers
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import bot


class Module(bot.Module):

    index = 'safeshare'

    def register(self):

        self.addcommand(
            self.safeshare,
            "safeshare",
            "Generate safeshare.tv link for YouTube and Vimeo videos.",
            ["[-description=description]", "[-title=title]", "[-end=end]",
             "[-start=start]", "url"]
        )

    def safeshare(self, context, args):

        payload = {
            'url': args.getstr('url'),
        }
        if 'title' in args:
            payload['title'] = args.getstr('title')
        if 'description' in args:
            payload['description'] = args.getstr('description')
        if 'start' in args:
            payload['start'] = int(args.getstr('start'))
        if 'end' in args:
            payload['end'] = int(args.getstr('end'))
        http = self.server.rget('http.url')
        response = http.request('http://safeshare.tv/api/generate',
                                code="GET", params=payload, body=None,
                                headers={}, timeout=None).json()
        return "%s" % ("http://safeshare.tv/v/" +
                       response['data'][0]['safeshare_id'])
bot.register.module(Module)
