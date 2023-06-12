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
            <rect rx={30} x={0} y={0} width={this.width} height={this.height} fill="rgb(101,139,148)" fillOpacity={.5}></rect>
            <text x={850} y={75} letterSpacing={-3} textLength={120} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">V/M</text>
            <text x={1600} y={75} textLength={30} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">H</text>
            <text x={1630} y={85} textLength={60} fontSize={30} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ЭШ</text>
            <text x={2070} y={75} textLength={150} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ВНИЗ</text>
            <text x={2055} y={800 - 90} textLength={180} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ВВЕРХ</text>
            <text x={3660} y={75} textLength={220} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ЗПУ/ЗК</text>
            <text x={4250} y={75} textLength={220} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ПУ-56М</text>
            <text x={3000} y={75} textLength={250} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">ОБР ЛУЧ</text>
            <g transform="translate(3785,640)">
                <circle r={140}></circle>
                <path d="M -330 20 l 135 0 l 50 -20" stroke="white" strokeWidth={5} fill="none"></path>
                <text x={-315} y={-30} textLength={110} fontSize={60} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="white" fill="white" fontFamily="lenya69">АВТ</text>
                <path d="M -330 20 l 135 0 l 50 -20" stroke="white" strokeWidth={5} fill="none"></path>
            </g>
        </g>
    }
}