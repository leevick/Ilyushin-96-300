import { Component } from "react";
import LeftLowerBG from "./LeftLower.png"

export default class LeftLower extends Component {
    constructor(props) {
        super(props)
        this.width = 4400
        this.heigh = 1000
        this.left = 0
        this.top = 0
    }

    render() {

        const r = 175
        const ca = 60
        const dr = 15

        var str = `M ${-r * Math.sin(Math.PI / 180 * ca)} ${-r * Math.cos(Math.PI / 180 * ca)} `

        for (var i = 1; i < 2 * ca - 4; i = i + 1) {
            str += `L ${(r - (i * dr / (2 * ca))) * Math.sin(Math.PI / 180 * (-ca + i))} ${-(r - (i * dr / (2 * ca))) * Math.cos(Math.PI / 180 * (-ca + i))} `
        }

        str += `A ${dr} ${dr} 0 0 0 ${(r + ((2 * ca - 5) * dr / (2 * ca))) * Math.sin(Math.PI / 180 * (-ca + (2 * ca - 5)))} ${-(r + ((2 * ca - 5) * dr / (2 * ca))) * Math.cos(Math.PI / 180 * (-ca + (2 * ca - 5)))} `

        for (var i = 2 * ca - 5; i >= 1; i = i - 1) {
            str += `L ${(r + (i * dr / (2 * ca))) * Math.sin(Math.PI / 180 * (-ca + i))} ${-(r + (i * dr / (2 * ca))) * Math.cos(Math.PI / 180 * (-ca + i))} `
        }

        return <g id="LeftLower" viewBox={`${this.left} ${this.top} ${this.width} ${this.heigh}`}>
            {/* <image href={LeftLowerBG}></image> */}
            <g>
                <text letterSpacing={-3} textLength={280} lengthAdjust="spacingAndGlyphs" x={3470} y={85} fontSize={70} fontFamily="lenya69" stroke="white" fill="white">ТОРМОЗА</text>
                <text letterSpacing={-3} textLength={190} lengthAdjust="spacingAndGlyphs" x={3800} y={85} fontSize={70} fontFamily="lenya69" stroke="white" fill="white">КОЛЕС</text>
            </g>
            <g transform="translate(3000,500)">
                <path d={str} strokeWidth={5} stroke="white" fill="none"></path>
            </g>
        </g>
    }

}