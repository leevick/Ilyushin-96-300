import { Component } from "react";


export default class SignalBoard extends Component {
    constructor(props) {
        super(props)
        this.name = props.name
    }

    render() {
        return <g>
            <g id={`${this.name}Emit`}></g>
            <g id="SignalBoard" viewBox="0 0 260 160">
                <rect x={0} y={0} width={260} height={160} fillOpacity={1} fill="rgb(10,10,10)"></rect>
            </g>
        </g>
    }
}