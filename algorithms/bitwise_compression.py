class CompressedCountry:
    def __init__(self, countries_csv: str) -> None:
        self.decoded_country_ISO: dict[str, int] = {
            "ARG": 0b00,
            "CMR": 0b01,
            "DEU": 0b10,
            "GAH": 0b11,
            "HKG": 0b100,
        }
        self.encoded_country_ISO: dict[int, str] = {
            0b00: "ARG",
            0b01: "CMR",
            0b10: "DEU",
            0b11: "GAH",
            0b100: "HKG",
        }
        self._compress(countries_csv)

    def _compress(self, countries_csv: str) -> None:
        """
        Get the binary representation for each country code.
        Use bitwise left shift operator to add these bits to a bit string.
        """
        self.bit_string: int = 1  # 0000 0001

        for country in countries_csv.upper().split(","):
            self.bit_string <<= 3  # 0000 1000

            if country in self.decoded_country_ISO:
                # DEU is 0b10
                # 0000 0100
                # 0000 0010 |= 0000 0110 = 6
                self.bit_string |= self.decoded_country_ISO[country]
            elif country == "":
                continue
            else:
                raise ValueError("Invalid nucleotide: {}".format(country))

    def decompress(self) -> str:
        """
        Get string representation for each country code.
        Use bitwise right shift operator to add these strings to a list.
        Reverse the list to return it in the right order again.
        """
        countries: list[str] = []

        for i in range(0, self.bit_string.bit_length() - 1, 3):
            bits: int = self.bit_string >> i & 0b111

            if bits in self.encoded_country_ISO:
                countries.append(self.encoded_country_ISO[bits])
            else:
                raise ValueError("Invalid bits: {}".format(bits))

        return str(countries[::-1])

    def __str__(self) -> str:
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof

    original: str = "ARG,CMR,DEU,GAH,HKG,DEU,ARG,GAH,HKG,CMR,DEU,GAH," * 100
    print("Original is {} bytes".format(getsizeof(original)))

    compressed: CompressedCountry = CompressedCountry(original)
    print("Compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)
