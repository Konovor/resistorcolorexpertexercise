def resistor_label(colors):
    UNIT = 'ohms'
    codas = []
    colars = {"black":'0',"brown":'1',"red":'2',"orange":'3',"yellow":'4',"green":'5',"blue":'6',"violet":'7',"grey":'8',"white":'9'}
    zeros = {"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9,}
    tolers = { "grey": "0.05%","violet":"0.1%","blue":"0.25%","green":" ±0.5%","brown":"1%","red":"2%","gold":"5%", }
    if len(colors)==1:
        return "0 ohms"
    if len(colors)==4:
        for i in range(0,2):
            codas.append(colars[colors[i]])
        plier = zeros[colors[2]]
        tocod = " ±"+tolers[colors[3]]
    elif len(colors)==5:
        for i in range(0,3):
            codas.append(colars[colors[i]])
        plier = int(colars[colors[3]])
        tocod = " ±"+tolers[colors[4]]

    if tocod == " ± ±0.5%":
        tocod = " ±0.5%"

    if colors[-1] == "silver":
        tocod = " ±10%"

    ccode = "".join(codas)
    value_ccode = int(ccode)
    value_ccode = value_ccode*(10 **plier)
    
    if value_ccode < 1000:
        return str(value_ccode)+ " " + UNIT + tocod
    else:
        if value_ccode >= 10**9:
            ohm_val = value_ccode/10**9
            if ohm_val == int(ohm_val):
                return f"{int(ohm_val)} gigaohms" + tocod
            else:
                return f"{ohm_val} gigaohms" + tocod
        elif value_ccode >= 10**6:
            ohm_val = value_ccode/10**6
            if ohm_val == int(ohm_val):
                return f"{int(ohm_val)} megaohms" + tocod
            else:
                return f"{ohm_val} megaohms" + tocod
        else:
            ohm_val = value_ccode/10**3
            if ohm_val == int(ohm_val):
                return f"{int(ohm_val)} kiloohms" + tocod
            else:
                return f"{ohm_val} kiloohms" + tocod
    return str(value_ccode)+ " ohms" + tocod

    return "0 ohms"
