import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-offer-details',
  templateUrl: './offer-details.component.html',
  styleUrls: ['./offer-details.component.css']
})
export class OfferDetailsComponent implements OnInit {
  offer: any = null;

  constructor(private route: ActivatedRoute, private http:HttpClient) { }
  ngOnInit(): void {
    const routeParams = this.route.snapshot.paramMap;
    const offerIdFromRoute = Number(routeParams.get('offerId'))
    this.loadOffer(offerIdFromRoute)
  }

  loadOffer(id:number) {
    this.http.get(`http://127.0.0.1:8000/api/offers/${id}`).subscribe((offer: any) => {
    this.offer = offer
    });
  }

}
