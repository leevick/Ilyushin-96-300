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

function getAllIds(root) {
    var ret = []
    if (root.hasAttribute("id")) {
        if (root.getAttribute("id") !== "root") {
            ret.push(root.getAttribute("id"))
        }
    }

    for (var n of root.childNodes) {
        if (n.nodeType === NodeType.ELEMENT_NODE) {
            ret = ret.concat(getAllIds(n))
        }
    }
    return ret
}

function export_svg(t) {
    const html = fs.readFileSync("./build/index.html", 'utf-8')
    const root = parse(html)

    const fd = fs.openSync(`./build/${t}.svg`, "w+")
    var svg = root.querySelector(`#${t}`)
    removeChildHasId(svg)
    const vb = svg.getAttribute("viewBox")

    const width = parseFloat(vb.split(' ')[2])
    const height = parseFloat(vb.split(' ')[3])


    fs.writeSync(fd, '<?xml version="1.0" encoding="UTF-8"?>')
    fs.writeSync(fd, `<svg width="${width / 10}mm" height="${height / 10}mm" viewBox="${vb}">`)
    fs.writeSync(fd, svg.toString())
    fs.writeSync(fd, "</svg>")
    fs.close(fd)
}

const html = fs.readFileSync("./build/index.html", 'utf-8')
const root = parse(html)

const ids = getAllIds(root)

console.log(ids)

for (const i of ids) {
    export_svg(i)
}


