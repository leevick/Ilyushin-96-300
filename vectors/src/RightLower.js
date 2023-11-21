import { Component } from "react";
import CabinAltimeter from "./cabin_altimeter.png"
import CabinAlt from "./CabinAlt.js";

export default class RightLower extends Component {
    constructor(props) {
        super(props)
        this.width = 4400
        this.heigh = 1000
        this.left = 0
        this.top = 0
    }

    render() {

        return <g id="LeftLower" viewBox={`${this.left} ${this.top} ${this.width} ${this.heigh}`}>
            <g transform="translate(1600,500)">
                <CabinAlt></CabinAlt>
            </g>
        </g>
    }

}