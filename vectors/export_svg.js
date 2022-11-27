#!/usr/bin/node
import { NodeType, parse } from 'node-html-parser'
import fs from 'fs'


function removeChildHasId(root) {
    for (var n of root.childNodes) {
        if (n.nodeType === NodeType.ELEMENT_NODE && n.hasAttribute("id")) {
            root.removeChild(n)
        } else {
            removeChildHasId(n)
        }
    }
}

const t = process.argv.slice(2)[0]

const html = fs.readFileSync("./build/index.html", 'utf-8')
const root = parse(html)

const fd = fs.openSync(`./build/${t}.svg`, "w+")
var svg = root.querySelector(`#${t}`)
removeChildHasId(svg)
const vb = svg.getAttribute("viewBox")

fs.writeSync(fd, '<?xml version="1.0" encoding="UTF-8"?>')
fs.writeSync(fd, `<svg viewBox="${vb}">`)
fs.writeSync(fd, svg.toString())
fs.writeSync(fd, "</svg>")
fs.close(fd)
