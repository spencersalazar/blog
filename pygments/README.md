
- Copy chuck.py to /Library/Ruby/Gems/2.0.0/gems/pygments.rb-0.6.3/vendor/pygments-main/pygments/lexers/

- Rebuild pygments lexer mapfile
    cd /Library/Ruby/Gems/2.0.0/gems/pygments.rb-0.6.3/vendor/pygments-main/; sudo make mapfiles

- Rebuild pygments.rb lexer cache
    cd /Library/Ruby/Gems/2.0.0/gems/pygments.rb-0.6.3/; sudo rake lexers

