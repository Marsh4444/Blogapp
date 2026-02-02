from .models import Category
from assignment.models import FollowUS


def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def get_follow_us(request):
    follow_us_links = FollowUS.objects.all()
    return {'follow_us_links': follow_us_links}
