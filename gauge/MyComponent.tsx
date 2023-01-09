import { FSComponent, DisplayComponent, VNode } from 'msfssdk';

export class MyComponent extends DisplayComponent<any> {
    public render(): VNode {
        return (
            <div class='my-component'>Hello World!</div>
        );
    }
}