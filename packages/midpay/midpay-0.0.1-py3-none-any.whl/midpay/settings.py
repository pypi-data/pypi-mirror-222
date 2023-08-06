BCA_VA = "bca_va"
BNI_VA = "bni_va"
PERMATA_VA = "permata_va"

VA_NAME_CHOICES = [BCA_VA, BNI_VA, PERMATA_VA]

VA_LINKS = {
    BCA_VA: {
        'inquiry_url': 'https://simulator.sandbox.midtrans.com/bca/va/inquiry',
        'payment_url': 'https://simulator.sandbox.midtrans.com/bca/va/payment',
    },
    BNI_VA: {
        'inquiry_url': 'https://simulator.sandbox.midtrans.com/bni/va/inquiry',
        'payment_url': 'https://simulator.sandbox.midtrans.com/bni/va/payment',
    },
    PERMATA_VA: {
        'inquiry_url': 'https://simulator.sandbox.midtrans.com/permata/va/inquiry',
        'payment_url': 'https://simulator.sandbox.midtrans.com/permata/va/payment',
    }
}
