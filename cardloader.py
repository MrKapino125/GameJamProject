import card

class Cardloader:
    def loadcard(self, id, screen, eventhandler, timer):
        match id:
            case 0:
                return card.ClickCard(screen, eventhandler, timer)
            case 1:
                return card.SliceCard(screen, eventhandler, timer)
            case 2:
                return card.MathCard(screen, eventhandler, timer)
            case 3:
                return card.RememberCard(screen, eventhandler, timer)
            case 4:
                return card.LabyrinthCard(screen, eventhandler, timer)
            case 5:
                return card.TriangleCard(screen, eventhandler, timer)
            case 6:
                return card.ImpossiblequizCard(screen, eventhandler, timer)
            case 7:
                return card.NotclickbuttonCard(screen, eventhandler, timer)
            case 8:
                return card.MessageCard(screen, eventhandler, timer)
            case 9:
                return card.RightCard(screen, eventhandler, timer)
            case 10:
                return card.MinefieldCard(screen, eventhandler, timer)
            case 11:
                return card.PressCard(screen, eventhandler, timer)
            case 12:
                return card.ColorCard(screen, eventhandler, timer)

