import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {
  constructor(private http: HttpClient) {}
  offers: any[] = [];
  myValue: number = 0;
  ngOnInit() {
    this.loadOffers();
  }
  loadOffers() {
    this.http
      .get('http://127.0.0.1:8000/api/offers')
      .subscribe((offers: any) => {
        this.offers = offers;
      });
  }
  loadOffer(offer: any) {
    this.http
      .get(`http://127.0.0.1:8000/api/offers/${offer.id}`)
      .subscribe((offer: any) => {});
  }
  loadOffer1(event: Event) {
    const target = event.target as HTMLInputElement;
    let targetValue = target.value;
    if (targetValue == '0') {
      targetValue = '';
    }
    this.http
      .get(`http://127.0.0.1:8000/api/offers?category=${targetValue}`)
      .subscribe(
        (offers: any) => {
          this.offers = offers;
        },
        (error) => {
          this.offers = []
        }
      );
  }
}
