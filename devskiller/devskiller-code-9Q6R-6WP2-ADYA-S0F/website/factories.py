import factory
import faker
from faker import providers

from leave import models

fake = faker.Faker()


class TestEmailProvider(providers.BaseProvider):
    def devskiller_email(self):
        return f"{self.generator.user_name()}@devskiller.com"


factory.Faker.add_provider(TestEmailProvider)


class UserFactory(factory.DjangoModelFactory):
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("devskiller_email")
    username = factory.Sequence(lambda n: fake.user_name() + str(n))
    is_staff = False
    is_active = True

    class Meta:
        model = models.User
