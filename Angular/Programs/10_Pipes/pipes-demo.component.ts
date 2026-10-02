import { CurrencyPipe, DatePipe, JsonPipe, PercentPipe, SlicePipe, UpperCasePipe } from '@angular/common';
import { Component, Pipe, PipeTransform } from '@angular/core';

// A custom pipe: shortens long text
@Pipe({ name: 'truncate' })
export class TruncatePipe implements PipeTransform {
  transform(value: string, limit = 10): string {
    return value.length > limit ? value.slice(0, limit) + '...' : value;
  }
}

@Component({
  selector: 'app-root',
  imports: [CurrencyPipe, DatePipe, JsonPipe, PercentPipe, SlicePipe, UpperCasePipe, TruncatePipe],
  template: `
    <p>Upper: {{ course | uppercase }}</p>
    <p>Price: {{ price | currency: 'INR' : 'symbol' : '1.2-2' }}</p>
    <p>Date: {{ launch | date: 'dd MMM yyyy' }}</p>
    <p>Discount: {{ discount | percent }}</p>
    <p>First two: {{ cities | slice: 0 : 2 }}</p>
    <p>Truncated: {{ about | truncate: 14 }}</p>
    <p>Chained: {{ launch | date: 'MMMM' | uppercase }}</p>
    <pre>{{ student | json }}</pre>
  `,
})
export class PipesDemoComponent {
  course = 'angular pipes';
  price = 1299.5;
  launch = new Date(2026, 0, 26); // 26 January 2026
  discount = 0.256;
  cities = ['Chennai', 'Madurai', 'Trichy', 'Salem'];
  about = 'Pipes transform values for display';
  student = { name: 'Arun', marks: [82, 91] };
}
