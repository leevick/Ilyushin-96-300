
import { Component, React } from "react"
import { SPSH4 } from "./SPSH4.js"
import SignalBoard from "./SignalBoard.js"

export class CentralRightPanel extends Component {
    constructor(props) {
        super(props)
    }

    render() {
        return <g id="CentralRightPanel" viewBox="0 0 1350 4300">
            <rect opacity={0.3} width={1350} height={4300} fill="white"></rect>
            <g transform="translate(40,515)">
                <SPSH4></SPSH4>

            </g>
            <g transform={`translate(210,240)`}>
                <g transform="translate(147.5,82.5)">
                    <g transform="translate(0,0)">
                        <rect stroke="white" strokeWidth={10} x={-147.5} y={-82.5} width={295} height={165} fillOpacity={1.0}></rect>
                        <g id="GearOnPower" viewBox="-120 -65 240 130">
                            <text x={-62.5} y={-30} fontWeight={"bold"} letterSpacing={-3} textLength={125} fontSize={50} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="rgb(0,255,0)" fill="rgb(0,255,0)" fontFamily="lenya69">ШАССИ</text>
                            <text x={-87.5} y={30} fontWeight={"bold"} letterSpacing={-3} textLength={175} fontSize={50} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="rgb(0,255,0)" fill="rgb(0,255,0)" fontFamily="lenya69">ПОД ТОК</text>
                        </g>
                    </g>

                    <g transform="translate(295,0)">
                        <rect stroke="white" strokeWidth={10} x={-147.5} y={-82.5} width={295} height={165} fillOpacity={1.0}></rect>
                        <g id="SteerDevice1" viewBox="-120 -65 240 130">
                            <text x={-75} y={-30} fontWeight={"bold"} letterSpacing={-3} textLength={150} fontSize={50} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="rgb(0,0,255)" fill="rgb(0,0,255)" fontFamily="lenya69">РУЛЕЖН</text>
                            <text x={-75} y={30} fontWeight={"bold"} letterSpacing={-3} textLength={150} fontSize={50} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="rgb(0,0,255)" fill="rgb(0,0,255)" fontFamily="lenya69">УСТР. 1</text>
                        </g>
                    </g>

                    <g transform="translate(590,0)">
                        <rect stroke="white" strokeWidth={10} x={-147.5} y={-82.5} width={295} height={165} fillOpacity={1.0}></rect>
                        <g id="SteerDevice2" viewBox="-120 -65 240 130">
                            <text x={-75} y={-30} fontWeight={"bold"} letterSpacing={-3} textLength={150} fontSize={50} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="rgb(0,0,255)" fill="rgb(0,0,255)" fontFamily="lenya69">РУЛЕЖН</text>
                            <text x={-75} y={30} fontWeight={"bold"} letterSpacing={-3} textLength={150} fontSize={50} lengthAdjust="spacingAndGlyphs" dominantBaseline="central" stroke="rgb(0,0,255)" fill="rgb(0,0,255)" fontFamily="lenya69">УСТР. 2</text>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    }
}