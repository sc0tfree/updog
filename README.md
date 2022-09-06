<p>
  <img src="https://sc0tfree.squarespace.com/s/updog.png" width=85px alt="updog"/>
</p>

Updog is a replacement for Python's `SimpleHTTPServer`. 
It allows uploading and downloading via HTTP/S, 
can set ad hoc SSL certificates and use HTTP basic auth.

## Installation

Install using pipx:

`pipx install git+https://github.com/KFDCompiled/updog`

## Usage

`updog [-d DIRECTORY] [-p PORT] [--password PASSWORD] [--ssl]`

| Argument                            | Description                                      |
|-------------------------------------|--------------------------------------------------| 
| -d DIRECTORY, --directory DIRECTORY | Root directory [Default=.]                       | 
| -p PORT, --port PORT                | Port to serve [Default=9090]                     |
| --password PASSWORD                 | Use a password to access the page. (No username) |
| --ssl                               | Enable transport encryption via SSL              |
| --version                           | Show version                                     |
| -h, --help                          | Show help                                        |

## Examples

**Serve from your current directory:**

`updog`

**Serve from another directory:**

`updog -d /another/directory`

**Serve from port 1234:**

`updog -p 1234`

**Password protect the page:**

`updog --password examplePassword123!`

*Please note*: updog uses HTTP basic authentication.
To login, you should leave the username blank and just
enter the password in the password field.

**Use an SSL connection:**

`updog --ssl`

**Upload using curl:**
`curl -v -XPOST -F "file=@PATH/NAME;filename=NAME" -F "path=/FULL/PATH/TO/UPDOG/WORKINGDIR" http://IP:PORT/upload`

if you started updog with `updog -p 80 -d ${PREFIX}/www` then `curl -v -XPOST -F "file=@Public/foo;filename=foo" -F "path=${PREFIX}/www" http://192.168.122.59:80/upload`



## Thanks

A special thank you to [Nicholas Smith](http://nixmith.com) for
designing the updog logo.
