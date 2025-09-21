from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
import random
from datetime import date, timedelta


class Command(BaseCommand):
    """Custom management command to seed the database with sample data."""

    help = "Seed the database with sample Listings, Bookings, and Reviews."

    def handle(self, *args, **kwargs):
        # Clear existing data (optional)
        Listing.objects.all().delete()
        Booking.objects.all().delete()
        Review.objects.all().delete()

        self.stdout.write("Seeding database with sample data...")

        # Create sample Listings
        listings = []
        for i in range(5):
            listing = Listing.objects.create(
                title=f"Sample Listing {i+1}",
                description=f"This is the description for listing {i+1}.",
                price=random.randint(50, 500)
            )
            listings.append(listing)

        # Create Bookings and Reviews for each Listing
        for listing in listings:
            # Create 2 bookings per listing
            for j in range(2):
                check_in = date.today() + timedelta(days=random.randint(1, 30))
                check_out = check_in + timedelta(days=random.randint(1, 5))
                Booking.objects.create(
                    listing=listing,
                    guest_name=f"Guest {j+1} for {listing.title}",
                    check_in=check_in,
                    check_out=check_out
                )

            # Create 2 reviews per listing
            for k in range(2):
                Review.objects.create(
                    listing=listing,
                    reviewer_name=f"Reviewer {k+1} for {listing.title}",
                    rating=random.randint(1, 5),
                    comment=f"This is review {k+1} for {listing.title}."
                )

        self.stdout.write(self.style.SUCCESS("✅ Database successfully seeded!"))
