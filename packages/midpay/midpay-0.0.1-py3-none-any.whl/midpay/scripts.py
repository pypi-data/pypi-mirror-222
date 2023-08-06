import click

from midpay.settings import VA_NAME_CHOICES
from midpay.crawlers import get_mid_simulator_class, do_process


@click.command()
@click.argument("va_name", type=click.Choice(VA_NAME_CHOICES))
@click.argument("va_number", type=click.STRING)
def cli(va_name, va_number):
    mid_class = get_mid_simulator_class(va_name, va_number)
    do_process(mid_class)
