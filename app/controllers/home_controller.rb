class HomeController < ApplicationController

  def index
    our_input_text = " Hola tu..."
    @hello = `python lib/assets/python/hello.py "#{our_input_text}"`

    @searches = Search.all

  end
end
