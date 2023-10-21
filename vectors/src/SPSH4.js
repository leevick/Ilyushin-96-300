
import { Component, React } from "react"

export class SPSH4 extends Component {
    constructor(props) {
        super(props)
        this.width = 650
        this.height = 650
        this.top = 0
        this.left = 0
        this.bevelWidth = 162.5
    }

    render() {
        return <g id="SPSH4">
            <path d={`M ${this.bevelWidth} 0 
            l ${this.width - 2 * this.bevelWidth} 0 
            l ${this.bevelWidth} ${this.bevelWidth}
            l ${0} ${this.width - 2 * this.bevelWidth}
            l ${-this.bevelWidth} ${this.bevelWidth}
            l ${-this.width + 2 * this.bevelWidth} ${0}
            l ${-this.bevelWidth} ${-this.bevelWidth}
            l ${0} ${-this.width + 2 * this.bevelWidth}
            Z`} color={"black"} fill={"black"} stroke={"black"} strokeWidth={10} />

            <path d="M 200 490 l 0 -130
                        c 0 -90 70 -190 100 -215 
                        c 15 -15 35 -15 50 0 
                        c 30 25 100 125 100 215
                        l 0 130
            " stroke="white" strokeWidth={8} fill="none"></path>
            <text letterSpacing={-3} textLength={150} lengthAdjust="spacingAndGlyphs" x={250} y={375} dominantBaseline="central" fontSize={50} fill="white" stroke="white" strokeWidth={2} fontFamily="lenya69">ШАССИ</text>
            <line x1={150} y1={490} x2={500} y2={490} strokeWidth={8} stroke="white"></line>
            <circle cx={325} cy={95} r={30} fill="#00ff00"></circle>
            <circle cx={325} cy={530} r={30} fill="#00ff00"></circle>
            <circle cx={325 - 165} cy={455} r={30} fill="#00ff00"></circle>
            <circle cx={325 + 165} cy={455} r={30} fill="#00ff00"></circle>
            <circle cx={325 - 85} cy={325} r={30} fill="#ffff00"></circle>
            <circle cx={325 + 85} cy={325} r={30} fill="#ffff00"></circle>
            <circle cx={325} cy={425} r={30} fill="#ffff00"></circle>
            <circle cx={325} cy={205} r={30} fill="#ffff00"></circle>
        </g>
    }
}