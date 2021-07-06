![GitHub release (latest by date)](https://img.shields.io/github/v/release/sc0tfree/updog?color=success&style=flat-square)
![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg?style=flat-square)
![GitHub](https://img.shields.io/github/license/crstian19/updog?color=blue&logoColor=blue&style=flat-square)
![Docker Pulls](https://img.shields.io/docker/pulls/crstian/updog?logo=Docker&style=flat-square)
![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/crstian/updog?logo=Docker&style=flat-square)
<p>
  <img src="https://sc0tfree.squarespace.com/s/updog.png" width=85px alt="updog"/>
</p>

Updog is a replacement for Python's `SimpleHTTPServer`. 
It allows uploading and downloading via HTTP/S, 
can set ad hoc SSL certificates and use HTTP basic auth.

<p align="center">
  <img src="https://sc0tfree.squarespace.com/s/updog-screenshot.png" alt="Updog screenshot"/>
</p>

## Installation

Install using pip:

`pip3 install updog`

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

## Thanks

A special thank you to [Nicholas Smith](http://nixmith.com) for
designing the updog logo.
