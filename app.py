from lxml import etree

# fname = 'test.txt'
f_inputname = './input/7705sar8_6.2.r4.txt'
f_outputname = './output/7705sar8_6.2.r4.xml'



# create XML root
root = etree.Element('root')

# DOM map. This list stores XML elements with list index corresponding to XML Elemet's DOM level
# so <root> element has 0 level, <admin> element has 1 level (i.e. [1] index)
map = [root]


with open(f_inputname, 'r') as finput:
    for str in finput.readlines():
        if str.rstrip():  # skip black lines

            # split line by '+' char. If no char is present, first elem of a tuple will have the whole string
            parsed_str = str.partition('+')

            # no '+' is present means that we have a string with '|' chars only.
            if parsed_str[1] is '':
                currentDOMLevel = parsed_str[0].count('|')  # count how many '|' is there, thats the DOM level
            else:
                # if map list already has element on currentDOMLevel index then we can use it
                if len(map)-1 >= currentDOMLevel:
                    map[currentDOMLevel] = etree.SubElement(map[currentDOMLevel-1], parsed_str[2].strip('-\n'))
                else:   # otherwise extend map list
                    map.append(etree.SubElement(map[currentDOMLevel-1], parsed_str[2].strip('-\n')))

# print(etree.tounicode(root, pretty_print=True))

with open(f_outputname, 'w') as foutput:
    foutput.write(etree.tounicode(root, pretty_print=True))