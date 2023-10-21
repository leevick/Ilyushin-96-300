
import { Component, React } from "react"
import { SPSH4 } from "./SPSH4.js"

export class CentralRightPanel extends Component {
    constructor(props) {
        super(props)
    }

    render() {
        return <g id="CentralRightPanel">
            <rect opacity={0.3} width={1350} height={4300} fill="white"></rect>
            <g transform="translate(40,515)">
                <SPSH4></SPSH4>
            </g>
        </g>
    }
}