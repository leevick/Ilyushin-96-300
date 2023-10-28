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

function export_svg(t, src, dst) {
    const html = fs.readFileSync(src, 'utf-8')
    const root = parse(html)

    const fd = fs.openSync(`${dst}/${t}.svg`, "w+")
    var svg = root.querySelector(`#${t}`)
    var images = svg.querySelectorAll('image');
    var i = 0;
    for (i = 0; i < images.length; i = i + 1) {
        images[i].setAttribute('xlink:href', images[i].getAttribute('href').substring(1))
        images[i].removeAttribute('href')
    }

    removeChildHasId(svg)
    const vb = svg.getAttribute("viewBox")

    const width = parseFloat(vb.split(' ')[2])
    const height = parseFloat(vb.split(' ')[3])


    fs.writeSync(fd, '<?xml version="1.0" encoding="UTF-8"?>')
    fs.writeSync(fd, `<svg version="1.1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg" width="${width / 10}mm" height="${height / 10}mm" viewBox="${vb}">`)
    fs.writeSync(fd, svg.toString())
    fs.writeSync(fd, "</svg>")
    fs.close(fd)
}

const sourceFile = process.argv.slice(2)[0]
const destDir = process.argv.slice(2)[1]

const html = fs.readFileSync(sourceFile, 'utf-8')
const root = parse(html)

const ids = getAllIds(root)

for (const i of ids) {
    export_svg(i, sourceFile, destDir)
}


