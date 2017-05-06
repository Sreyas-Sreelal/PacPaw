
# src/pacpaw.py - main module

"""

PacPaw a python based package manager for pawn language.
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

VERSION = "1.0";
BANNER = """

          ██████╗  █████╗  ██████╗██████╗  █████╗ ██╗    ██╗
          ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██║    ██║
          ██████╔╝███████║██║     ██████╔╝███████║██║ █╗ ██║
          ██╔═══╝ ██╔══██║██║     ██╔═══╝ ██╔══██║██║███╗██║
          ██║     ██║  ██║╚██████╗██║     ██║  ██║╚███╔███╔╝
          ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝     ╚═╝  ╚═╝ ╚══╝╚══╝ 
                               {version %s alpha}                             
""" %(VERSION);

@click.group( invoke_without_command = True )
@click.pass_context


def cli( ctx ):
        if ctx.invoked_subcommand is None:
                sys_send.print_yellow( BANNER );
                print("\n\n");
                print( "Usage : pacpaw [OPTIONS] COMMANDS [ARGS]\n" );
                print( "Use --help to see all available commands" );
                pass


@click.command( help = 'Provides sa-mp function\'s definitions' )
@click.option( '--name', prompt = 'Your function name',
              help = 'The function to refer.' )


def refer( name ): 
    GetFunction( name );


@click.command( help = 'Gets samp repo' )

@click.option( 
                '--name','-S', 
                prompt='Script\'s name',
                help='Name of sa-mp script.' 
              )

@click.option( 
                '--listversion' , '-lv' , 
                is_flag = True,
                help = 'List the available versions of package'
              )

def getscript( name , listversion ):
        GetRepo( name ,listversion);


@click.command( help = 'Gets samp snippet' )
@click.option( '--name','-S', prompt = 'Snippet\'s name',
              help = 'Name of sa-mp snippet.')


def getsnippet( name ):
        GetSnippet( name );


# initialising commandline

cli.add_command( refer );
cli.add_command( getscript );
cli.add_command( getsnippet );


if __name__ == '__main__':
	cli( );
