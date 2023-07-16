def crc_encode(message, polynomial):
    message = list(message)
    polynomial = list(polynomial)
    dividend = message + ['0'] * (len(polynomial) - 1)

    for i in range(len(message)):
        if dividend[i] == '1':
            for j in range(len(polynomial)):
                dividend[i + j] = str(int(dividend[i + j]) ^ int(polynomial[j]))

    return ''.join(dividend[-len(message):])


def crc_check(message, polynomial):
    remainder = crc_encode(message, polynomial)
    return '0' * (len(polynomial) - 1) == remainder


def main():
    message = input("Enter the binary message: ")
    polynomial = input("Enter the polynomial: ")
    encoded_message = crc_encode(message, polynomial)
    print("Encoded message:", encoded_message)

    received_message = input("Enter the recieved message: ")
    print("Received message:", received_message)

    error_detected = crc_check(received_message, polynomial)

    if error_detected:
        print("Error detected during transmission.")
    else:
        print("No error detected during transmission.")


if __name__ == "__main__":
    main()
