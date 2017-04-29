
"""
Samp Helper a python based package manager for samp built with the power of web scraping.
Developer : Sreyas (__SyS__) : https://github.com/Sreyas-Sreelal
Contributors / Collabrators : None

"""
import click
import requests
from bs4 import BeautifulSoup
import sys_send
from gistscrap import GetSnippet
from githubreposcrap import GetRepo
from function_search import GetFunction
import click 

Version = "1.0";


@click.group(invoke_without_command=True)
@click.pass_context

def cli(ctx):
        if ctx.invoked_subcommand is None:
                print("PacPaw Build" + Version );
                print("Usage : pacpaw [OPTIONS] COMMANDS [ARGS]\n");
                print("Use --help to see all available commands");
                pass

@click.command(help='Provides sa-mp function\'s definitions')
@click.option('--name', prompt='Your function name',
              help='The function to refer.')

def refer(name): 
    GetFunction( name );

@click.command(help='Gets samp repo')
@click.option('--name', prompt='Script\'s name',
              help='Name of sa-mp script.')
def getscript(name):
        GetRepo(name);

@click.command(help='Gets samp snippet')
@click.option('--name', prompt='Snippet\'s name',
              help='Name of sa-mp snippet.')
def getsnippet(name):
        GetSnippet(name);

cli.add_command(refer);
cli.add_command(getscript);
cli.add_command(getsnippet);


if __name__ == '__main__':
	cli();
