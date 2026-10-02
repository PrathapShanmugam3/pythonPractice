// Run with: npx tsx rxjs-basics.ts
import { filter, interval, lastValueFrom, map, Observable, of, Subject, take, tap } from 'rxjs';

async function main() {
  // 1. Creation + operators in pipe()
  of(1, 2, 3, 4, 5, 6)
    .pipe(
      filter((n) => n % 2 === 0), // keep even numbers
      map((n) => n * 10), // multiply by 10
    )
    .subscribe((v) => console.log('even x10:', v));

  // 2. Build your own Observable (note the cleanup function)
  const greeting$ = new Observable<string>((subscriber) => {
    subscriber.next('Hello');
    subscriber.next('Angular');
    subscriber.complete();
    return () => console.log('cleanup done');
  });
  greeting$.subscribe({
    next: (v) => console.log('got:', v),
    complete: () => console.log('stream completed'),
  });

  // 3. Subject: push values manually; every subscriber receives them
  const bell$ = new Subject<string>();
  bell$.subscribe((m) => console.log('Student A heard:', m));
  bell$.subscribe((m) => console.log('Student B heard:', m));
  bell$.next('Class over!');

  // 4. Timed stream: 3 ticks, 50 ms apart, then it completes
  const last = await lastValueFrom(
    interval(50).pipe(
      take(3),
      map((i) => i + 1),
      tap((n) => console.log('tick', n)),
    ),
  );
  console.log('last tick was', last);
}

main();
