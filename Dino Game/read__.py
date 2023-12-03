import tkinter as tk

root = tk.Tk()
root.geometry("250x170")

T = tk.Text(root, height=250, width=170)
l = tk.Label(root, text="YOGA")
l.config(font=("Courier", 14))
Fact = """Yoga is essentially a spiritual discipline based on an extremely subtle Science which focuses on bringing harmony between mind and body. It is an art and science for healthy living. The word "Yoga" is derived from the Sanskrit root yuj meaning "to join", "to yoke" or "to unite".
According to Yogic scriptures, the practice of Yoga leads to the union of individual consciousness with universal consciousness. According to modern scientists, everything in the universe is just a manifestation of the same quantum firmament. One who experiences this oneness of existence is said to be "in Yoga" and is termed as a yogi who has attained a state of freedom, referred to as Mukti, nirvāna, kaivalya or moksha.
"Yoga" also refers to an inner science comprising of a variety of methods through which human beings can achieve union between the body and mind to attain self-realisation. The aim of Yoga practice (sādhana) is to overcome all kinds of sufferings that lead to a sense of freedom in every walk of life with holistic health, happiness and harmony.
Brief history and development of Yoga
The science of Yoga has its origin thousands of years ago, long before the first religion or belief systems were born. According toYogic lore, Shiva has seen as the first yogi or ādiyogi and the first guru or ādiguru. Several thousand years ago, on the banks of lake Kantisarovar in the Himalayas, ādiyogi poured his profound knowledge into the legendary saptarishis or "seven sages". These sages carried this powerful Yogic science to different parts of the world including Asia, the Middle East, northern Africa and South America. Interestingly, modern scholars have noted and marvelled at the close parallels found between ancient cultures across the globe. However, it was in India that the Yogic system found its fullest expression. Agastya, the saptarishi who travelled across the Indian subcontinent, crafted this culture around a core Yogic way of life.
Yoga is widely considered as an "immortal cultural outcome" of the Indus Saraswati Valley Civilisation – dating back to 2700 BC – and has proven itself to cater to both material and spiritual uplift of humanity. A number of seals and fossil remains of Indus Saraswati Valley Civilisation with Yogic motifs and figures performing Yoga sādhana suggest the presence of Yoga in ancient India. The seals and idols of mother Goddess are suggestive of Tantra Yoga. The presence of Yoga is also available in folk traditions, Vedic and Upanishadic heritage, Buddhist and Jain traditions, Darshanas, epics of Mahabharata including Bhagawadgita and Ramayana, theistic traditions of Shaivas, Vaishnavas and Tantric traditions. Though Yoga was being practiced in the pre-Vedic period, the great sage Maharishi Patanjali systematised and codified the then existing Yogic practices, its meaning and its related knowledge through Patanjali's Yoga Sutras.
After Patanjali, many sages and Yoga masters contributed greatly for the preservation and development of the field through well documented practices and literature. Yoga has spread all over the world by the teachings of eminent Yoga masters from ancient times to the present date. Today, everybody has conviction about Yoga practices towards the prevention of disease, maintenance and promotion of health. Millions and millions of people across the globe have benefitted by the practice of Yoga and the practice of Yoga is blossoming and growing more vibrant with each passing day.
The Fundamentals of Yoga
Yoga works on the level of one's body, mind, emotion and energy. This has given rise to four broad classifications of Yoga: Karma Yoga where we utilise the body; Jnāna Yoga where we utilise the mind; Bhakti Yoga where we utilise the emotion and Kriya Yoga where we utilise the energy. Each system of Yoga we practice falls within the gamut of one or more of these categories.
Every individual is a unique combination of these four factors. Only a guru (teacher) can advocate the appropriate combination of the four fundamental paths as is necessary for each seeker. "All ancient commentaries on Yoga have stressed that it is essential to work under the direction of a guru."
Traditional schools of Yoga
The different philosophies, traditions, li neages and guru-shishya paramparas of Yoga led to the emergence of different traditional schools. These include Jnāna Yoga, Bhakti Yoga, Karma Yoga, Pātanjala Yoga, Kunḍ ạ lini Yoga, Haṭha Yoga, Dhyāna Yoga, Mantra Yoga, Laya Yoga, Rāja Yoga, Jain Yoga, Bouddha Yoga etc. Each school has its own approach and practices that lead to the ultimate aim and objectives of Yoga.
Yogic practices for health and wellness
The widely practiced Yoga sadhanas are: Yama, Niyama, Āsana, Prānāyāma, Pratyāhara, Dhārana, Dhyāna, Samādhi, Bandhas and Mudras, Shatkarmas, Yuktāhāra, Mantra-japa, Yukta-karma etc. Yamas are restraints and Niyamas are observances. These are considered to be pre-requisites for further Yogic practices. Āsanas, capable of bringing about stability of body and mind, "kuryat-tadasanam- sthairyam", involve adopting various psycho-physical body patterns and giving one an ability to maintain a body position (a stable awareness of one's structural existence) for a considerable length of time.
Prānāyāma consists of developing awareness of one's breathing followed by willful regulation of respiration as the functional or vital basis of one's existence. It helps in developing awareness of one's mind and helps to establish control over the mind. In the initial stages, this is done by developing awareness of the "flow of in-breath and out-breath" (svāsa-prasvāsa) through nostrils, mouth and other body openings, its internal and external pathways and destinations. Later, this phenomenon is modified, through regulated, controlled and monitored inhalation (svāsa) leading to the awareness of the body space getting filled (puraka), the space(s) remaining in a filled state (kumbhaka) and it getting emptied (rechaka) during regulated, controlled and monitored exhalation(prasvāsa).
Pratyāhara indicates dissociation of one's consciousness (withdrawal) from the sense organswhich connect with the external objects. Dhārana indicates broad based field of attention (inside the body and mind) which is usually understood as concentration.
Dhyāna (meditation) is contemplation (focussed attention inside the body and mind) and Samādhi (integration).
Bandhas and Mudras are practices associated with Prānāyāma. They are viewed as the higher yogic practices that mainly adopt certain physical gestures along with control over respiration. This further facilitates control over mind and paves way for higher Yogic attainment. However, practice of dhyāna, which moves one towards self-realisation and leads one to transcendence, is considered the essence of Yoga Sādhana.
Śaṭkarmas are detoxification procedures that are clinical in nature and help to remove the toxins accumulated in the body. Yuktāhāra advocates appropriate food and food habits for healthy living."""



l.pack()
T.pack()


T.insert(tk.END, Fact)
tk.mainloop()

