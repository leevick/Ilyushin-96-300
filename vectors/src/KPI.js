import { Component } from "react"


export class KPI extends Component {

    constructor(props) {
        super(props)
        this.width = 1600
        this.height = 1600
        this.left = -800
        this.top = -800

        this.ahWidth = 400


    }
    render() {
        return <g id="KPI" viewBox={`${this.left} ${this.top} ${this.width} ${this.height}`}>
            {/* <rect x={-800} y={-800} width={1600} height={1600} fill="black"></rect> */}
            <rect x={-this.ahWidth / 2} y={-this.ahWidth / 2}
                width={this.ahWidth} height={this.ahWidth} fill="rgb(28,161,254)"></rect>
            <rect x={-this.ahWidth / 2} y={-this.ahWidth / 2}
                width={this.ahWidth} height={this.ahWidth} fill="rgb(128,55,43)"></rect>
        </g>
    }
}