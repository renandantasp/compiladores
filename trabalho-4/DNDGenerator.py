import os

class PageGenerator:
    def __init__(self, symbols, path):
        self.symbols = symbols
        self.path = path

    def createPage(self):
        if not os.path.isdir(self.path):
            os.mkdir(self.path)
        css = self.createCSS()
        with open(f"{self.path}/style.css", "w") as f:
            f.write(css)
        start_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <title>Spells</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@300;400&family=Roboto+Slab:wght@400;500&family=Roboto:wght@300&display=swap" rel="stylesheet"></head>
<body>
"""     
        html_spell = """<div class="spell">
        <h2>#NAME#</h2>
        <div class="flex #SCHOOL#">
            <div class="item">
                <p><span>LEVEL</span><br>#LEVEL#</p>
            </div>
            <div class="item">
                <p><span>SCHOOL</span><br>#SCHOOL#</p>
            </div>
            <div class="break"></div>
            """
        opt_tag = """<div class="item">
                <p><span>TAG</span><br>$VALUE$</p>
            </div>"""
        bl = """<div class="break">"""
        quant_opt = 0
        end_spell = """</div>            
        </div>
        <p class="desc">#DESCR#</p>
    </div>"""
        end_html = """</body></html>"""
        html = start_html
        for scopes, symbol in self.symbols.items():
            spell = html_spell

            opt = ""
            for atr, value in symbol.items():
                if atr == 'level' or atr == 'name' or atr == 'school':
                    spell = spell.replace(f"#{atr.upper()}#", str(value))
                elif atr == 'cast':
                    print(str(value))
                    copy = opt_tag
                    copy = copy.replace("TAG", "CAST").replace("$VALUE$", str(value))
                    opt = opt + copy
                elif atr == 'dmg':
                    copy = opt_tag
                    copy = copy.replace("TAG", "DAMAGE").replace("$VALUE$", str(value))
                    opt = opt + copy
                elif atr == 'dmg_type':
                    copy = opt_tag
                    copy = copy.replace("TAG", "DAMAGE TYPE").replace("$VALUE$", str(value))
                    opt = opt + copy
                elif atr == 'comp':
                    copy = opt_tag
                    copy = copy.replace("TAG", "COMPONENTS").replace("$VALUE$", str(value))
                    opt = opt + copy
     
                
            html = html + spell + opt + end_spell
            html = html.replace('#DESCR#', symbol['descr'])
            

        
        html = html + end_html
        with open(f"{self.path}/index.html", "w") as f:
            f.write(html)

    def createCSS(self):
        return """body{
    margin-top: 0px;
    margin-left: 10vw;
    margin-right: 10vw;
}
h2{ font-family: 'Roboto Slab', serif; }
p,span{ font-family: 'Roboto Condensed', sans-serif; }
p{font-weight: 400;}
span{font-weight: 700;}
.spell{
    margin-top: 0px;
    padding: 10px;
}
.break{
    width: 100%;
}
.flex{
    display: flex;
    padding:10px;
    flex-wrap: wrap;
    border: 1px #aaaaaa solid;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
    border-top: 4px #888888 solid;
}
.item{
    padding-left: 4vw;
    padding-right: 4vw;
}

.Necromancy{
    border-top-color: #9bd928 ;
}

.Abjuration{
    border-top-color: #28cdd9 ;
}

.Evocation{
    border-top-color: #aa2000 ;
}


        """
        