import { Component } from "react";
import pu56 from "./pu56.png"


export default class PU56 extends Component {
    constructor(props) {
        super(props)
        this.width = 4600
        this.height = 800
        this.left = 0
        this.top = 0
    }

    render() {
        return <g id="PU56" viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            <image x={216} y={0} width={4384} height={800} href={pu56} />
            <rect rx={30} x={0} y={0} width={this.width} height={this.height} fill="rgb(101,139,148)" fillOpacity={1}></rect>
            <text x={850} y={75} letterSpacing={-3} textLength={120} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">V/M</text>
            <text x={1600} y={75} textLength={30} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">H</text>
            <text x={1630} y={85} textLength={60} fontSize={30} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ЭШ</text>
            <text x={2070} y={75} textLength={150} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ВНИЗ</text>
        </g>
    }
}