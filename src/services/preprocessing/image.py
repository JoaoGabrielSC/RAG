from torchvision import transforms


class ImagePreprocessor:
    IMAGE_SIZE = (224, 224)
    MEAN = [0.485, 0.456, 0.406]
    STD = [0.229, 0.224, 0.225]

    @staticmethod
    def get_default_transform() -> transforms.Compose:
        """
        Returns the default image transformation pipeline used for
        most pretrained models (e.g., ResNet, ViT from torchvision/huggingface).

        Returns:
            torchvision.transforms.Compose: A composed transform ready to use.
        Example:
            >>> transform = ImagePreprocessor.get_default_transform()
            >>> print(transform)
            Compose(
                Resize(size=(224, 224), interpolation=bilinear, max_size=None, antialias=warn)
                ToTensor()
                Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
            )
        """

        tranform = transforms.Compose(
            [
                transforms.Resize(ImagePreprocessor.IMAGE_SIZE),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=ImagePreprocessor.MEAN, std=ImagePreprocessor.STD
                ),
            ]
        )

        return tranform
