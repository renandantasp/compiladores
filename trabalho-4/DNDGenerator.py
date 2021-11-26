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
            """
        opt_tag = """<div class="item">
                <p><span>TAG</span><br>$VALUE$</p>
            </div>"""
        bl = """<div class="break"></div>"""
        end_spell = """</div>            
        </div>
        <p class="desc">#DESCR#</p>
    </div>"""
        end_html = """</body></html>"""
        html = start_html
        for scopes, symbol in self.symbols.items():
            spell = html_spell

            opt = ""
            quant_opt = 0
            for atr, value in symbol.items():
                if  atr == 'name' or atr == 'school':
                    spell = spell.replace(f"#{atr.upper()}#", str(value))
                elif atr == 'level':
                    val = str(value)
                    if val == '1':
                        val = val + 'st'
                    elif val == '2':
                        val = val + 'nd'
                    elif val == '3':
                        val = val + 'rd'
                    else:
                        val = val + 'th'
                    spell = spell.replace(f"#{atr.upper()}#", val)
                elif atr == 'cast':
                    quant_opt = quant_opt + 1
                    copy = opt_tag
                    copy = copy.replace("TAG", "CAST").replace("$VALUE$", str(value))
                    opt = opt + copy
                elif atr == 'damage':
                    quant_opt = quant_opt + 1
                    copy = opt_tag
                    copy = copy.replace("TAG", "DAMAGE").replace("$VALUE$", str(value))
                    opt = opt + copy
                elif atr == 'dmg_type':
                    quant_opt = quant_opt + 1
                    copy = opt_tag
                    copy = copy.replace("TAG", "DAMAGE TYPE").replace("$VALUE$", str(value))
                    opt = opt + copy
                elif atr == 'comp':
                    quant_opt = quant_opt + 1
                    val = str(value).replace("(","<i>(").replace(")",")</i>")
                    copy = opt_tag
                    copy = copy.replace("TAG", "COMPONENTS").replace("$VALUE$", val)
                    opt = opt + copy
                if quant_opt == 1:
                    opt = opt + bl
     
                
            html = html + spell + opt + end_spell
            html = html.replace('#DESCR#', symbol['descr'])
            

        
        html = html + end_html
        with open(f"{self.path}/index.html", "w") as f:
            f.write(html)

    def createCSS(self):
        return """body{
    background: #23272a;
    margin-top: 0px;
    margin-left: 5vw;
    margin-right: 25vw;
}

h2{ font-family: 'Roboto Slab', serif; color:#cfdbe6}
p,span{ font-family: 'Roboto Condensed', sans-serif; color:#cfdbe6}
span{color:#cfdbe6}
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
    justify-content: flex-start;
    background: #2c2f33;
    padding:10px;
    flex-wrap: wrap;
    
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
    border-top: 4px #888888 solid;
    box-shadow: 5px 10px 8px #1c1f23; 
}
.item{
    padding-left: 4vw;
    padding-right: 4vw;
}
.desc{
    color:#cfdbe6;
    margin: 20px 20px 0px 20px;
    padding-bottom:20px;
    border-bottom: 2px #3e4146 solid;
}
.Divination  { border-top-color: #BFDBFE }
.Abjuration  { border-top-color: #60A5FA }
.Necromancy  { border-top-color: #9b74f2 }

.Conjuration { border-top-color: #D97706 }
.Illusion    { border-top-color: #FBBF24 }
.Evocation   { border-top-color: #f04747 }

.Enchantment  { border-top-color: #EC4899 }
.Transmutation{ border-top-color: #ff73fa }


"""
        