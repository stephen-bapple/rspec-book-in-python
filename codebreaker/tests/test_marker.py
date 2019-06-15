from unittest import TestCase, main
from expects import expect, equal

from codebreaker.marker import Marker


class TestMarkerExactMatchCount(TestCase):
    def test_exact_match_count_with_no_matches(self):
        marker = Marker('1234', '5555')
        expect(marker.exact_match_count()).to(equal(0))

    def test_exact_match_count_with_1_exact_match(self):
        marker = Marker('1234', '1555')
        expect(marker.exact_match_count()).to(equal(1))

    def test_exact_match_count_with_1_number_match(self):
        marker = Marker('1234', '2555')
        expect(marker.exact_match_count()).to(equal(0))

    def test_exact_match_count_with_1_exact_and_1_number_match(self):
        marker = Marker('1234', '1525')
        expect(marker.exact_match_count()).to(equal(1))


class TestMarkerNumberMatchCount(TestCase):
    def test_number_match_count_with_no_matches(self):
        marker = Marker('1234', '5555')
        expect(marker.number_match_count()).to(equal(0))

    def test_number_match_count_with_1_number_match(self):
        marker = Marker('1234', '2555')
        expect(marker.number_match_count()).to(equal(1))

    def test_number_match_count_with_1_exact_match(self):
        marker = Marker('1234', '1555')
        expect(marker.number_match_count()).to(equal(0))

    def test_number_match_count_with_1_exact_and_1_number_match(self):
        marker = Marker('1234', '1525')
        expect(marker.number_match_count()).to(equal(1))


if __name__ == "__main__":
    main()

