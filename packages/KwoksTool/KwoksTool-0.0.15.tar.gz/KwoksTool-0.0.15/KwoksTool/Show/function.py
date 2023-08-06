def SelecTHead(html,dict):
    text_single = '''<div data-v-6e2a8889="" style="display: inline-block;position: relative;cursor: pointer;height: 26px;line-height: 26px;border: 1px solid #000000;color: #000000;background: #b8c0e0;padding: 0 8px;font-size: 12px;margin-left: 5px;margin-top: 4px" onclick="window.open('显示地址','_self')">显示名称<!----></div>'''
    text_sum = text_single.replace('显示名称', dict[0]['名称']).replace('显示地址', dict[0]['地址'])
    for i in range(1,len(dict)):
        text_single='''<div data-v-6e2a8889="" style="display: inline-block;position: relative;cursor: pointer;height: 26px;line-height: 26px;border: 1px solid #000000;color: #000000;background: #b8c0e0;padding: 0 8px;font-size: 12px;margin-left: 5px;margin-top: 4px" onclick="window.open('显示地址','_self')">显示名称<!----></div>'''
        text_sum=text_sum+text_single.replace('显示名称',dict[i]['名称']).replace('显示地址',dict[i]['地址'])
    text_sum='''        <!--=========================================-->
    <div class="box" style="background-color: #000649;width: 1565px;height:100px">
        <!--=========================================-->
<div ">'''+text_sum+'''</div>
</div>
<!--=========================================-->'''
    with open(html, "r", encoding="utf8") as f:
        f=f.read()
    f=f.replace('    <div class="box">',text_sum)
    with open(html,'w',encoding='utf-8') as ff:
        ff=ff.write(f)
    return text_sum