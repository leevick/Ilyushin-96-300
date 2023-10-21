import { Component } from "react";
import main from "./main.jpg"

export class MainPanel extends Component {
    constructor(props) {
        super(props)
        this.width = 1000
        this.height = 1000
        this.left = 0
        this.top = 0
    }

    render() {

        return <g id="MAIN" viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            <g transform="scale(21.4)">
                <g transform="translate(-130,-340)">
                    <image href={main}></image>
                </g>
            </g>
        </g>
    }
}