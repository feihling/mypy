'''
Created on 2015-3-24

@author: lingfeihua
'''
import xml.dom.minidom
import sys
#import xml.dom.Node

# def scanNode(node, oid_list=[]):
#     if node.nodeType == xml.dom.Node.ELEMENT_NODE:
#         if node.tagName == 'entity':
#             cur_oid = node.getAttribute('oid')
#             if cur_oid not in oid_list:
#                 print cur_oid
#                 oid_list.append(cur_oid)
#                 for oid in oid_list:
#                     tmpfile.write(oid)
#                 tmpfile.write('\n')            
#         if node.tagName == 'field':
#             for oid in oid_list:
#                 tmpfile.write(oid)
#             tmpfile.write(node.getAttribute('oid'))
#             tmpfile.write('\n')
# 
#     if node.hasChildNodes():
#         for child in node.childNodes:
#             scanNode(child, oid_list)
#         if node.nodeType == xml.dom.Node.ELEMENT_NODE:
#             if node.tagName == 'entity':
#                 oid_list.pop()

def scanNode(node, oid_list=[]):
    if node.nodeType == xml.dom.Node.ELEMENT_NODE:
        if node.tagName == 'entity':
            cur_oid = node.getAttribute('oid')
            oid_list.append(cur_oid)
            for oid in oid_list:
                tmpfile.write(oid)
            tmpfile.write('\n')            
        if node.tagName == 'field':
            for oid in oid_list:
                tmpfile.write(oid)
            tmpfile.write(node.getAttribute('oid'))
            tmpfile.write('\n')

    if node.hasChildNodes():
        for child in node.childNodes:
            cur_oid_list = oid_list[:]
            scanNode(child, cur_oid_list)

# xml_doc = xml.dom.minidom.parse('configuration-structure.xml')
# tmpfile = open('test.log', 'w')
# scanNode(xml_doc)
# tmpfile.close()
